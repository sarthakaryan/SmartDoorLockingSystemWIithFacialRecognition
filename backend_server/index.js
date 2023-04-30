const express = require('express');
const multer = require('multer');
const { spawn } = require('child_process')
const { exec } = require('child_process')
var fs = require('fs');
const app = express();

const storage = multer.diskStorage({
  destination: function (req, file, cb) {
    cb(null, '../test_images/');
  },
  filename: function (req, file, cb) {
    cb(null, "test" + '.jpg');
  }
});
const upload = multer({ storage: storage });
app.post('/photos', upload.single('image'), (req, res) => {
  if (!req.file) {
    return res.status(400).send('No file uploaded');
  }

  const python = spawn('python', ["../main.py"])
  python.stdout.on('data', function (data) {
    console.log(data.toString())
    obj = JSON.parse(data.toString())
    if (obj.Distance < 1000) {
      res.status(200).send(`Name : ${obj.Name}\nPercent Match : ${((1000-obj.Distance)/10).toFixed(2)}%`);
      fs.cp('../test_images/test.jpg', `../training_images/${obj["Name"]}/${Date.now()}.jpg`, (err) => {
        if (err) {
          console.error(err);
        }
      });
    }
    else {
      res.status(200).send("Unrecognized Access Alert: Face recognition system failed to verify the presented face!");
    }

  })

});
app.use('/',(req,res)=>{
   res.end('Hello World!');
})
const port = process.env.PORT || 3000;
app.listen(port, () => {
  console.log(`Server running on port ${port}`);
});
