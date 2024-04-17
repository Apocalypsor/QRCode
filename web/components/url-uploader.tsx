import { Button } from "@nextui-org/button";
import { Card, CardBody, CardHeader } from "@nextui-org/card";
import { useState } from "react";

export default function UrlUploader({
    title,
    onUpload,
}: {
    title: string;
    onUpload: (url: string) => void;
}) {
    const [url, setUrl] = useState<string>("");

    const handleUrlChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        setUrl(e.target.value);
    };

    return (
        <div className="w-full max-w-md">
            <Card>
                <CardHeader>
                    <h2 className="text-lg font-semibold text-center">
                        {title}
                    </h2>
                </CardHeader>
                <CardBody>
                    <input
                        type="text"
                        value={url}
                        onChange={handleUrlChange}
                        className="w-full p-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
                        placeholder="https://example.com"
                    />
                    <Button
                        className="w-full mt-4 bg-blue-500 text-white p-2 rounded-lg hover:bg-blue-600"
                        onClick={() => {}}
                    >
                        Submit URL
                    </Button>
                </CardBody>
            </Card>
        </div>
    );
}
