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

First, Install zbar according to [this document](https://github.com/Eric-Canas/qreader).

Then, you can install the dependencies using the following command:
```bash
pip install -r requirements.txt
```

### Run the development server

```bash
python main.py
```

You can access api documentation at http://localhost:8000/docs.

### Test

```bash
pytest tests
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

First, you should have [pnpm](https://pnpm.io/installation) installed.

Then, run the following command:
```bash
pnpm install
```

#### Run the development server

```bash
pnpm run dev
```

Now, you can access the app at http://localhost:3000. The backend server should be running at http://localhost:8000 at the same time.

## License

Licensed under the [Apache License, Version 2.0](LICENSE).
