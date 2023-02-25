const { exec } = require('child_process');

exec('cd wp-hack && node Run.js'), (error, stdout, stderr) => {
  if (error) {
    console.error(exec error: ${error});
    return;
  }
  console.log(stdout: ${stdout});
  console.error(stderr: ${stderr});
});