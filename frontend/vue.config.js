const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  outputDir: "../backend/static/",
  assetsDir: process.env.NODE_ENVIRON === "prod"
    ? "../static"
    : ""
})
