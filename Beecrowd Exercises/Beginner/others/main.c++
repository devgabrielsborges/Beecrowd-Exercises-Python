const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.question('', (rw_input) => {
  rl.question('', (r_limit) => {
    let operations_counter = 0;
    let r_counter = 0;

    for (let k = 0; k < rw_input.length; k++) {
      const v = rw_input[k];
      if (v === 'W') {
        r_counter = 0;
        operations_counter++;
      } else if (v === 'R') {
        if (r_counter === 0) {
          r_counter++;
        }
        if (k < rw_input.length - 1 && rw_input[k + 1] === 'R' && r_counter < r_limit) {
          r_counter++;
        } else {
          r_counter = 0;
          operations_counter++;
        }
      }
    }

    console.log(operations_counter);
    rl.close();
  });
});
