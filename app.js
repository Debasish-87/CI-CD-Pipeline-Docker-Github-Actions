const express = require('express');
const app = express();
const port = 80;

app.get('/', (req, res) => {
  res.send('🚀 Hello from CI/CD Pipeline using GitHub Actions + Docker + Minikube!');
});

app.listen(port, () => {
  console.log(`App running on port ${port}`);
});
