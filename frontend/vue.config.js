const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  outputDir: "../backend/html/",
  assetsDir: process.env.NODE_ENVIRON === "prod"
    ? "../html"
    : ""
})
