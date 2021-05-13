const path = require("path");
const autoprefixer = require("autoprefixer");

module.exports = [
  {
    resolve: {
      modules: [
        path.resolve(__dirname, "blog_demo_django_app/static/js"),
        "node_modules",
      ],
    },
    mode: "production",
    entry: "bundle.js",
    output: {
      path: path.resolve(__dirname, "blog_demo_django_app/static/"),
      filename: "bundle.js",
    },
  },
  {
    module: {
      rules: [
        {
          test: /\.scss$/,
          use: [
            {
              loader: "postcss-loader",
              options: {
                postcssOptions: { plugins: [autoprefixer()] },
              },
            },
            {
              loader: "sass-loader",
              options: {
                sassOptions: {
                  includePaths: [
                    path.resolve(
                      __dirname,
                      "blog_demo_django_app/static/scss/"
                    ),
                    path.resolve(
                      __dirname,
                      "blog_demo_django_app/static/scss/"
                    ),
                  ],
                },
              },
            },
          ],
          type: "asset",
        },
      ],
    },
    resolve: {
      modules: [path.resolve(__dirname, "blog_demo_django_app/static/scss/")],
    },
    mode: "production",
    entry: "bundle.scss",
    output: {
      path: path.resolve(__dirname, "blog_demo_django_app/static/"),
      filename: "bundle.css.js",
      assetModuleFilename: "bundle.css",
    },
  },
];
