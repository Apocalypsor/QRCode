"use client";

import FileUploader from "@/components/file-uploader";
import UrlUploader from "@/components/url-uploader";
import { Card, CardBody, CardHeader } from "@nextui-org/card";
import { Divider } from "@nextui-org/divider";
import Image from "next/image";
import { useState } from "react";

export default function Parser() {
    const [parsedResult, setParsedResult] = useState<string | null>(null);
    const [image, setImage] = useState<string | null>(null);

    const handleUpload = (file: File) => {
        setParsedResult("123131232131231asfasfasfasf123123123123");
        setImage(URL.createObjectURL(file));
    };

    const handleUrlUpload = (url: string) => {
        setParsedResult(
            "123131232131231asfasfasfasf1231231231231231231232312321212.123123123123123",
        );
        setImage(url);
    };

    const UploadCards = (
        <>
            <FileUploader
                title={"Upload Your QR Code"}
                onUpload={handleUpload}
            />
            <UrlUploader
                title={"Enter URL of QR Code"}
                onUpload={handleUrlUpload}
            />
        </>
    );

    return (
        <div className={"flex flex-col items-center justify-center gap-4"}>
            <h2 className={"text-3xl font-semibold"}>Parse images & URLs</h2>

            <div className="flex gap-4 hidden md:flex">{UploadCards}</div>

            <div className="flex flex-col gap-4 md:hidden">{UploadCards}</div>

            {image && (
                <div className={"mt-8"}>
                    <Card>
                        <CardHeader
                            className={"flex flex-col break-words max-w-md"}
                        >
                            <b>Parsed Result</b>
                            <p className="break-all">{parsedResult}</p>
                        </CardHeader>
                        <Divider />
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
