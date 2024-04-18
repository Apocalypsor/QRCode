import { Button } from "@nextui-org/button";
import { Card, CardBody, CardHeader } from "@nextui-org/card";
import { Input } from "@nextui-org/input";
import React, { useState } from "react";

export default function UrlUploader({
    title,
    onUpload,
}: {
    title: string;
    onUpload: any;
}) {
    const [url, setUrl] = useState<string>("");

    const handleUrlChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        setUrl(e.target.value);
    };

    const isValidUrl = React.useMemo(() => {
        if (url === "") return true;
        try {
            new URL(url);
            return true;
        } catch (e) {
            return false;
        }
    }, [url]);

    return (
        <div className="w-full max-w-md p-4">
            <Card className="p-2">
                <CardHeader>
                    <h2 className="text-lg font-semibold text-center">
                        {title}
                    </h2>
                </CardHeader>
                <CardBody>
                    <Input
                        isClearable
                        type="text"
                        variant="bordered"
                        className={"w-full"}
                        value={url}
                        onClear={() => setUrl("")}
                        onChange={handleUrlChange}
                        placeholder="https://example.com"
                        isInvalid={!isValidUrl}
                        color={!isValidUrl ? "danger" : "default"}
                    />
                    <Button
                        className="w-full mt-4 bg-gradient-to-t from-[#5EA2EF] to-[#0072F5] text-white p-2 rounded-lg hover:bg-blue-800"
                        onClick={() => onUpload(url)}
                    >
                        Submit URL
                    </Button>
                </CardBody>
            </Card>
        </div>
    );
}
