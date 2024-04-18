import { NextRequest } from "next/server";

export async function GET(request: NextRequest) {
    return proxyRequest(request);
}

async function proxyRequest(request: NextRequest) {
    const url = new URL(request.nextUrl);
    const targetUrl = url.searchParams.get("url");

    if (!targetUrl) {
        return new Response(JSON.stringify({ error: "No URL provided" }), {
            status: 400,
            headers: {
                "Content-Type": "application/json",
            },
        });
    }

    try {
        const response = await fetch(targetUrl, {
            method: request.method,
            headers: request.headers,
        });

        return new Response(response.body, {
            status: response.status,
            headers: {
                "Access-Control-Allow-Origin": "*",
                ...response.headers,
            },
        });
    } catch (error: any) {
        return new Response(JSON.stringify({ error: error.message }), {
            status: 500,
            headers: {
                "Content-Type": "application/json",
            },
        });
    }
}
