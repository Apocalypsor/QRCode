# QR Code Parser & Generator

## Backend

### Technologies Used
- [FastAPI](https://fastapi.tiangolo.com/)
- [qreader](https://github.com/Eric-Canas/qreader)
- [qrcode](https://github.com/lincolnloop/python-qrcode)

### How to Use

```bash
cd api
```

#### Install dependencies

First, you should have [pipenv](https://pipenv.pypa.io/en/latest/installation.html) installed. If you don't have it, you can install it using the following command:
```bash
pip install pipenv
```

Also, Install zbar according to [this document](https://github.com/Eric-Canas/qreader).

Then, you can install the dependencies using the following command:
```bash
pipenv install
```

### Run the development server

```bash
pipenv run python main.py
```

### Test

```bash
pipenv run pytest tests
```

## Frontend

### Technologies Used

- [Next.js 13](https://nextjs.org/docs/getting-started)
- [NextUI v2](https://nextui.org/)
- [Tailwind CSS](https://tailwindcss.com/)
- [Tailwind Variants](https://tailwind-variants.org)
- [TypeScript](https://www.typescriptlang.org/)
- [Framer Motion](https://www.framer.com/motion/)
- [next-themes](https://github.com/pacocoursey/next-themes)

### How to Use

```bash
cd web
```

#### Install dependencies

```bash
pnpm install
```

#### Run the development server

```bash
pnpm run dev
```

## License

Licensed under the [Apache License, Version 2.0](LICENSE).
