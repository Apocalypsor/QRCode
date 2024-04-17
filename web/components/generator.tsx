"use client";

import { Button } from "@nextui-org/button";
import { Card, CardBody, CardHeader } from "@nextui-org/card";
import { Textarea } from "@nextui-org/input";
import QrSvg from "@wojtekmaj/react-qr-svg";
import React, { useState } from "react";

export default function Generator() {
    const [text, setText] = useState<string>("");
    const [image, setImage] = useState<string | null>(null);

    return (
        <div className="flex flex-col items-center justify-center gap-4">
            <h2 className={"text-3xl font-semibold"}>Generate QR Code</h2>

            <Card className={"w-2/3 md:w-2/5"}>
                <CardHeader>
                    <h2 className="text-lg font-semibold text-center">
                        {"You can enter your text here"}
                    </h2>
                </CardHeader>
                <CardBody>
                    <Textarea
                        value={text}
                        onChange={(e) => setText(e.target.value)}
                        placeholder="Text to encode in QR code"
                        minRows={4}
                    />
                    <Button
                        className="w-full mt-4 bg-blue-500 text-white p-2 rounded-lg hover:bg-blue-600"
                        onClick={() => {
                            setImage(text);
                        }}
                    >
                        Generate QR Code
                    </Button>
                </CardBody>
            </Card>

            {image && (
                <Card className="mt-8">
                    <CardBody>
                        <QrSvg value={image} width={300} />
                    </CardBody>
                </Card>
            )}
        </div>
    );
}
