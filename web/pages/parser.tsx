"use client";

import FileUploader from "@/components/file-uploader";
import UrlUploader from "@/components/url-uploader";
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

            <UrlUploader
                title={"Enter URL of QR Code"}
                onUpload={(url) => {
                    console.log(url);
                }}
            />

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
