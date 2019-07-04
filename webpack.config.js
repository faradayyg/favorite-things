const path = require('path');
const BrowserSyncPlugin = require('browser-sync-webpack-plugin');

module.exports = {
	entry: './src/js/app.js',
	  output: {
	    filename: 'app.js',
      path: __dirname + '/static/js',
      publicPath: '/static/js'
    },
  
  resolve: {
      extensions: [ '.js', '.vue'],
      alias: {
        'vue': 'vue/dist/vue.common.js',
        'src': path.resolve(__dirname, '../src'),
        'assets': path.resolve(__dirname, '../src/assets'),
        'components': path.resolve(__dirname, '../src/components'),
        '@': path.resolve(__dirname, 'src/js/')
      }

  },
  module:
  {
  	rules :[
	  	{
	        test: /\.vue$/,
	        loader: 'vue-loader'
	    },
      {
          test: /\.js$/,
          loader: 'babel-loader',
          exclude: '/node_modules/'
      },
      {
        test: /\.scss$/,
        loaders: ["style-loader", "css-loader", "sass-loader"]
      },
      {
        test: /\.less$/,
        use: [
          {
            loader: 'style-loader', // creates style nodes from JS strings
          },
          {
            loader: 'css-loader', // translates CSS into CommonJS
          },
          {
            loader: 'less-loader', // compiles Less to CSS
          },
        ]
      },
      {
        test: /\.css$/,
        include: /node_modules/,
        loaders: ['style-loader', 'css-loader'],
      }
    ]
  },
  plugins: [
    new BrowserSyncPlugin({
      host: 'localhost',
      port: 3000,
      proxy: 'http://localhost:8000/'
    })
  ],
  mode: 'development'
}