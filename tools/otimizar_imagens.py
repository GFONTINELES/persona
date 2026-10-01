"""Gera as versões WebP das fotos e capturas usadas no site.

Rode sempre que trocar uma imagem em assets/img/ ou assets/projects/:

    python tools/otimizar_imagens.py

Para cada JPG listado abaixo, cria <nome>-<largura>.webp na mesma pasta.
O navegador escolhe o tamanho certo para a tela (atributo srcset no index.html).
O JPG original não é alterado e continua como reserva para navegadores antigos.

Requer Pillow: pip install Pillow
"""

from pathlib import Path

from PIL import Image, ImageOps

RAIZ = Path(__file__).resolve().parent.parent

# Larguras precisam bater com os srcset do index.html.
IMAGENS = {
    "assets/img/hero-1.jpg": (480, 800, 1200),
    "assets/img/hero-2.jpg": (480, 800, 1200),
    "assets/img/hero-3.jpg": (480, 800, 1200),
    "assets/projects/projeto-1.jpg": (640, 1000, 1600),
    "assets/projects/projeto-2.jpg": (640, 1000, 1600),
}

QUALIDADE = 80
AVISO_KB = 600


def gerar(caminho: Path, larguras: tuple[int, ...]) -> None:
    with Image.open(caminho) as original:
        # Fotos de celular guardam a rotação no EXIF: aplica antes de redimensionar.
        imagem = ImageOps.exif_transpose(original).convert("RGB")

    if imagem.width < max(larguras):
        print(f"  aviso: {caminho.name} tem {imagem.width}px de largura; o ideal é pelo menos {max(larguras)}px")

    for largura in larguras:
        largura_final = min(largura, imagem.width)
        altura = round(imagem.height * largura_final / imagem.width)
        copia = imagem.resize((largura_final, altura), Image.Resampling.LANCZOS)
        destino = caminho.with_name(f"{caminho.stem}-{largura}.webp")
        copia.save(destino, "WEBP", quality=QUALIDADE, method=6)
        print(f"  {destino.relative_to(RAIZ).as_posix()}  {destino.stat().st_size // 1024} KB")


def main() -> None:
    for relativo, larguras in IMAGENS.items():
        caminho = RAIZ / relativo
        if not caminho.exists():
            print(f"faltando: {relativo}")
            continue
        tamanho_kb = caminho.stat().st_size // 1024
        print(f"{relativo} ({tamanho_kb} KB)")
        if tamanho_kb > AVISO_KB:
            print(f"  aviso: o JPG original passa de {AVISO_KB} KB; reduza para cerca de 300 KB")
        gerar(caminho, larguras)


if __name__ == "__main__":
    main()
