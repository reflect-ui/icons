# Resources Placeholder Directory

> This directory's items are ignored via `./.gitignore`. this directory's content is only popullated while running `tools/* ` scripts

### S3 Bucket

All resources open to public at: https://reflect-icons.s3.us-west-1.amazonaws.com/

```txt
├── README.md (this file)
├── all.json
├── list.json
├── (family).json
├── (family).dist.zip
├── antd.dist.zip
└── material.dist.zip
```

- all.json - all merged refelct icons configuration in single json file
- antd.dist.zip - antd icons svgs and config.json zipped
- material.dist.zip - material icons svgs and config.json zipped

### Resource URL Scheme

```
/<provider>/<icon>(?(\-|\_)<variant>).<ext>

- /material/3d_rotation.svg
- /material/3d_rotation_outline.svg
- /radix-ui/align-left.svg
- /radix-ui/align-left.svg
- /unicons/airplay.svg
```

| Field    | Description        | Example                           | Required |
| -------- | ------------------ | --------------------------------- | -------- |
| provider | icon provider name | material, antd, radix-ui, unicons | yes      |
| icon     | icon name          | 3d_rotation, align-left, airplay  | yes      |
| variant  | icon variant       | outline, filled, line             | no       |
| ext      | file extension     | svg, png, jpg                     | yes      |
