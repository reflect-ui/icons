import type { IconMeta } from "./types";

const uri = (name: string) => "https://icons.reflect-ui.com/radix-ui/" + name;

export default function map(names: Array<string>) {
  return names.map((name) => {
    return <IconMeta>{
      uri: uri(name),
      name: name,
      variants: [],
      size: 15,
      package: "radix-ui",
      version: 1,
      category: "User Interface",
      tags: [],
    };
  });
}
