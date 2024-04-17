"use client";

import { Button } from "@nextui-org/button";
import { Card, CardBody, CardHeader } from "@nextui-org/card";
import { Textarea } from "@nextui-org/input";
import React, { useState } from "react";

export default function QrGenerator() {
    const [url, setUrl] = useState<string>("");

    const handleUrlChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        setUrl(e.target.value);
    };

    return (
        <div className="w-1/3">
            <Card>
                <CardHeader>
                    <h2 className="text-lg font-semibold text-center">
                        {"You can enter your text here"}
                    </h2>
                </CardHeader>
                <CardBody>
                    <Textarea
                        value={url}
                        onChange={handleUrlChange}
                        placeholder="Text to encode in QR code"
                        multiple
                    />
                    <Button
                        className="w-full mt-4 bg-blue-500 text-white p-2 rounded-lg hover:bg-blue-600"
                        onClick={() => {}}
                    >
                        Generate QR Code
                    </Button>
                </CardBody>
            </Card>
        </div>
    );
}
