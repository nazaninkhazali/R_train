const I = require("./illus"); const fs = require("fs");
(async () => {
  const out = process.argv[2]; fs.mkdirSync(out, { recursive: true });
  for (const k of Object.keys(I)) { if (["P","toPng","_prim"].includes(k)) continue;
    const ill = k === "elisaWell" ? I[k](false) : I[k]();
    fs.writeFileSync(`${out}/${k}.png`, await I.toPng(ill, 900));
    if (k === "elisaWell") fs.writeFileSync(`${out}/elisaWellProblems.png`, await I.toPng(I.elisaWell(true), 900));
  }
})();
