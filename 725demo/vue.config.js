const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  publicPath: process.env.NODE_ENV === 'production'
    ? '/c-team/725demo/'
    : '/',
  transpileDependencies: true
})