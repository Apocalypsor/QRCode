"use client";

import FileUploader from "@/components/file-uploader";
import { Button } from "@nextui-org/button";
import { Card, CardBody, CardHeader } from "@nextui-org/card";
import Image from "next/image";
import { useState } from "react";

export default function Parser() {
    const [image, setImage]: [string, any] = useState("");

    const handleUpload = (file: File) => {
        console.log(file);
        setImage(URL.createObjectURL(file));
    };

    return (
        <div className={"flex flex-col items-center justify-center gap-4"}>
            <FileUploader
                title={"Upload Your QR Code Here"}
                onUpload={handleUpload}
            />

            <div className="w-full max-w-md">
                <Card>
                    <CardHeader>
                        <h2 className="text-lg font-semibold text-center">
                            Enter URL
                        </h2>
                    </CardHeader>
                    <CardBody>
                        <input
                            type="text"
                            value={"test"}
                            onChange={() => {}}
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

            {image && (
                <div>
                    <Card>
                        <CardHeader
                            className={"flex flex-col break-words max-w-md"}
                        >
                            <b>Parsed Result</b>
                            <p className="break-all">
                                123131232131231asfasfasfasf1231231231231231231232312321212.123123123123123
                            </p>
                        </CardHeader>
                        <CardBody className="flex justify-center items-center p-4">
                            <div className="flex justify-center items-center overflow-hidden rounded-lg max-w-full">
                                <Image
                                    src={image}
                                    alt="QR Code"
                                    width={300}
                                    height={300}
                                    className="object-cover"
                                />
                            </div>
                        </CardBody>
                    </Card>
                </div>
            )}
        </div>
    );
}
