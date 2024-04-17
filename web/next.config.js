/** @type {import('next').NextConfig} */
const nextConfig = {
    images: {
        remotePatterns: [
            {
                protocol: "https",
                hostname: "no-cors.apocalypse.workers.dev",
                port: "",
                pathname: "/**",
            },
        ],
    },
};

module.exports = nextConfig;
