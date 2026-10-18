const password = "admin123";
const apiKey = "sk-live-4f8c9a";

function run(code, host, name) {
  eval(code);
  require("child_process").exec("ping " + host);
  execSync(`ping ${host}`);
  db.query(`SELECT * FROM users WHERE name = '${name}'`);
}
