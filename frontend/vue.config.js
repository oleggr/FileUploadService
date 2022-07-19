const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  outputDir: "../backend/html/",
  assetsDir: process.env.NODE_ENVIRON === "prod"
    ? "../html"
    : "",
  pages: {
    index: {
      entry: 'src/uploader/main.js',
      filename: 'index.html',
      title: 'Index Page',
    },
    viewer: 'src/viewer/main.js',
  },
  // head: [
  //   ['link', { rel: "icon", type: "image/png", href: "/public/favicon-32x32.png"}],
  // ],
})
