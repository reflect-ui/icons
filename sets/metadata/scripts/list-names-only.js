let fs = require("fs");
const args = process.argv;
let i_raw = args[2];
let o_raw = args[3];
let i = i_raw.replace(/(.*?)=/g, "");
let o = o_raw.replace(/(.*?)=/g, "");

if (!i || !o) {
  throw "i & o flag is required to specify in & out file. (input file as json, output as txt)";
}

const raw = fs.readFileSync(i);
const json = JSON.parse(raw);

const keys = Object.keys(json);
const txt = keys.join("\n");

fs.writeFile(o, txt, function (err) {
  if (err) return console.log(err);
  console.log(`dump names complete. to ${o}`);
});
