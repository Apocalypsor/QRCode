"use client";

import { title } from "@/components/primitives";
import { apiConfig } from "@/config/site";
import { Button } from "@nextui-org/button";
import { Card, CardBody, CardHeader } from "@nextui-org/card";
import { Textarea } from "@nextui-org/input";
import axios from "axios";
import Image from "next/image";
import React, { useState } from "react";

export default function Generator() {
    const [text, setText] = useState<string>("");
    const [image, setImage] = useState<string | null>(null);

    const handleGenerate = async (text: string) => {
        try {
            const res = await axios.post(
                apiConfig.url + "generate-qr",
                {
                    text,
                },
                {
                    responseType: "arraybuffer",
                    headers: {
                        "Content-Type": "application/json",
                    },
                },
            );

            // Create a new Blob object from the response data
            const blob = new Blob([res.data], { type: "image/png" });

            // Create an object URL for the Blob object
            const objectURL = URL.createObjectURL(blob);

            // Set the image state to the object URL
            setImage(objectURL);
        } catch (error) {
            console.error(error);
        }
    };

    return (
        <div className="flex flex-col items-center justify-center gap-4">
            <h1 className={title({ color: "cyan" })}>Generate QR Code</h1>

            <Card className={"w-full md:w-2/5"}>
                <CardHeader>
                    <h2 className="text-lg font-semibold text-center">
                        {"You can enter text here"}
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
                        className="w-full mt-4 bg-gradient-to-t from-[#00b7fa] to-[#01cfea] text-white p-2 rounded-lg hover:bg-cyan-800"
                        onClick={() => {
                            handleGenerate(text).then(() => {
                                console.log("QR code generated");
                            });
                        }}
                    >
                        Generate QR Code
                    </Button>
                </CardBody>
            </Card>

            {image && (
                <Card className="mt-8">
                    <CardBody>
                        <Image
                            src={image}
                            width={300}
                            height={300}
                            alt="QR code"
                        />
                    </CardBody>
                </Card>
            )}
        </div>
    );
}
