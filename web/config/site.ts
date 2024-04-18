export type SiteConfig = typeof siteConfig;

export const siteConfig = {
    name: "QR Code",
    description: "Pure front-end QR code parser/generator",
    navItems: [
        {
            label: "Parser",
            href: "/",
        },
        {
            label: "Generator",
            href: "/generator",
        },
    ],
};
