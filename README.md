# Portfólio: Gabriel Fontineles

Site estático (HTML + CSS), sem build. Abre direto no navegador.

## Estrutura

```
portfolio/
├── index.html              conteúdo da página
├── styles.css              visual
├── 404.html                página de endereço inexistente
├── robots.txt, sitemap.xml para buscadores
├── favicon.*, apple-touch-icon.png   ícones
├── _headers                cabeçalhos HTTP (Cloudflare Pages e Netlify)
├── tools/
│   └── otimizar_imagens.py gera as versões .webp das fotos
└── assets/
    ├── fonts/              fontes do site (.woff2)
    ├── img/                fotos do topo (hero-1/2/3.jpg) e imagem de compartilhamento (og-image.jpg)
    ├── projects/           capturas de tela dos projetos e capa do vídeo
    └── video/              vídeos de demonstração (.mp4) e legendas (.vtt)
```

As fotos, capturas e o vídeo em `assets/` são exemplos. **Substitua mantendo o mesmo nome** e depois rode o script de imagens (abaixo).

## Rodar no VS Code

1. Abra a pasta: `File > Open Folder` e escolha `portfolio`.
2. Instale a extensão **Live Server** (o VS Code vai sugerir ao abrir a pasta).
3. Clique com o botão direito em `index.html` e escolha **Open with Live Server**.

## O que editar

Procure por `[` em `index.html` (Ctrl+F): tudo entre colchetes é para preencher.

- Resultado de cada projeto: um número real (tempo poupado, erros evitados, usuários).
- Aprendizado de cada projeto: o que aquele trabalho te ensinou.
- `[ano]`, marcos da trajetória, parágrafo pessoal e depoimentos.
- **Ferramentas e práticas** (seção Trajetória): mantenha só o que você usa e sabe explicar.
- Textos dos projetos e da seção de aprendizados são rascunhos: reescreva com as suas palavras.

O código dos projetos não é publicado: cada projeto é mostrado por capturas ou gravação de tela, com a explicação logo abaixo.

Para adicionar um projeto, copie um bloco `<article class="project">` inteiro.

### Currículo

Salve o PDF como `assets/curriculo-gabriel-fontineles.pdf`. O link "Currículo (PDF)" no rodapé já aponta para ele.

### Fotos e vídeos

- Fotos do topo: JPG, cerca de 1200 px de largura, até 300 KB cada.
- Capturas dos projetos: JPG, proporção 16:10 (ex.: 1600 x 1000).
- **Depois de trocar qualquer foto ou captura, rode:**

  ```
  pip install Pillow          (só na primeira vez)
  python tools/otimizar_imagens.py
  ```

  O script cria versões `.webp` em vários tamanhos, que são as que o navegador realmente mostra. Se esquecer, o site continua exibindo as imagens antigas.
- Vídeos: MP4 (H.264), de 30 a 90 segundos, até uns 15 MB. Para reduzir uma gravação de tela sem som:
  `ffmpeg -i original.mov -vf scale=1280:-2 -crf 26 -an assets/video/projeto-3.mp4`
  (com narração, tire o `-an`, que remove o áudio).
- Legendas: se o vídeo tiver narração, escreva as falas no `.vtt` de mesmo nome (instruções dentro do arquivo). Gravação sem fala não precisa.
- Imagem de compartilhamento: `assets/img/og-image.jpg` (1200 x 630) aparece quando o link é enviado no LinkedIn ou WhatsApp.

### Cuidado com dados da empresa

Antes de publicar capturas e vídeos de projetos do trabalho, confirme com a empresa se podem ser exibidos e esconda ou troque valores, nomes de clientes e fornecedores, códigos internos e qualquer dado sensível.

## Antes de publicar

- [ ] Nenhum `[` sobrando no `index.html`
- [ ] Fotos, capturas e vídeo reais no lugar, e `python tools/otimizar_imagens.py` rodado
- [ ] Currículo em `assets/curriculo-gabriel-fontineles.pdf`
- [ ] Data em `sitemap.xml` (`<lastmod>`) atualizada

## Publicar em gabrielfontineles.com.br

1. **Registre o domínio** em registro.br (precisa de CPF ou CNPJ; confira o valor anual no site).
2. **Suba o projeto para o GitHub** (repositório novo, pasta `portfolio` como raiz).
3. **Hospede de graça** em Cloudflare Pages, Netlify ou GitHub Pages: conecte o repositório. Não há comando de build; a pasta de publicação é a raiz (`/`).
   - Cloudflare Pages e Netlify leem o `_headers` (segurança e cache) e usam o `404.html` sozinhos. O GitHub Pages ignora o `_headers`, sem causar erro.
4. **Aponte o domínio**: no painel da hospedagem, adicione `gabrielfontineles.com.br` e `www.gabrielfontineles.com.br` e copie os valores de DNS que ele mostrar. No registro.br, em DNS do domínio, crie esses registros (normalmente um `A` ou `ALIAS` para o domínio raiz e um `CNAME` para o `www`).
5. Aguarde a propagação (de minutos a algumas horas). O HTTPS é emitido automaticamente.
6. **Cadastre o site no Google Search Console** e envie o `sitemap.xml`.

Depois disso, cada `git push` atualiza o site.

### Analytics (opcional)

Escolha depois de definir a hospedagem. Cloudflare Web Analytics (se usar Cloudflare Pages) ou Netlify Analytics funcionam sem banner de cookies. Ao adicionar o script, libere o domínio dele no `Content-Security-Policy` do `_headers`.
