const I = require("./illus"); const fs = require("fs");
(async () => {
  const out = process.argv[2]; fs.mkdirSync(out, { recursive: true });
  for (const k of Object.keys(I)) { if (["P","toPng","_prim"].includes(k)) continue;
    fs.writeFileSync(`${out}/${k}.png`, await I.toPng(I[k](), 1000));
  }
})();
