const express = require('express');
const pathToSwaggerUi = require('swagger-ui-dist').absolutePath();

const app = express();

const fileName = 'test.json';
const filePath = './' + fileName;

// route
app.use('/apiref', express.static(pathToSwaggerUi));
app.use('/' + fileName, function(req, res) {
	res.json(require(filePath));
})

// redirect to file path
app.use('/api', function(req, res) {
	res.redirect('/apiref?url=/' + fileName);
})

app.listen(3000, () => console.log('Swagger listening on port 3000!'));