const { createProxyMiddleware } = require('http-proxy-middleware');

module.exports = function(app) {
    app.use(
        '/api',
        createProxyMiddleware({
            target: 'http://localhost:8080', // Adjust if your API server is on a different port
            changeOrigin: true,
        })
    );
};
