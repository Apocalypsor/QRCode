"use client";

import FileUploader from "@/components/file-uploader";
import { title } from "@/components/primitives";
import UrlUploader from "@/components/url-uploader";
import { apiConfig } from "@/config/site";
import { Button } from "@nextui-org/button";
import { Card, CardBody, CardHeader } from "@nextui-org/card";
import { Divider } from "@nextui-org/divider";
import { Textarea } from "@nextui-org/input";
import {
    Modal,
    ModalBody,
    ModalContent,
    ModalFooter,
    ModalHeader,
    useDisclosure,
} from "@nextui-org/modal";
import { Spinner } from "@nextui-org/spinner";
import axios from "axios";
import Image from "next/image";
import qrcodeParser from "qrcode-parser";
import { useState } from "react";

export default function Parser() {
    const [parsedResult, setParsedResult] = useState<string | null>(null);
    const [image, setImage] = useState<string | null>(null);
    const [loading, setLoading] = useState<boolean>(false);
    const { isOpen, onOpen, onOpenChange } = useDisclosure();

    const handleUpload = async (file: File) => {
        setImage(null);
        setLoading(true);
        try {
            const result = await qrcodeParser(file);
            setParsedResult(result);
            setImage(URL.createObjectURL(file));
        } catch (e) {
            setImage(null);
            onOpen();
        }

        setLoading(false);
    };

    const handleUrlUpload = async (url: string) => {
        setImage(null);
        setLoading(true);

        const timeout = (ms: number) =>
            new Promise((_, reject) =>
                setTimeout(() => reject(new Error("Request timed out")), ms),
            );

        try {
            const result = (await Promise.race([
                axios.post(apiConfig.url + "parse-qr-from-url", { url }),
                timeout(3000),
            ])) as { data: string };

            setParsedResult(result.data);
            setImage("https://no-cors.apocalypse.workers.dev/" + url);
        } catch (e) {
            console.error(e);
            setImage(null);
            onOpen();
        }

        setLoading(false);
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
            <h1 className={title()}>
                Parse&nbsp;
                <span className={title({ color: "violet" })}>images&nbsp;</span>
                and&nbsp;
                <span className={title({ color: "blue" })}>URLs&nbsp;</span>
            </h1>

            <div className="gap-4 hidden md:flex">{UploadCards}</div>

            <div className="flex flex-col gap-4 md:hidden">{UploadCards}</div>

            {loading && <Spinner size="lg" aria-label="Loading..." />}

            {image && (
                <div className={"mt-8"}>
                    <Card>
                        <CardHeader
                            className={"flex flex-col break-words max-w-md"}
                        >
                            <b>Parsed Result</b>
                            <Textarea
                                value={parsedResult || ""}
                                className={"mt-2"}
                                isReadOnly
                            />
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

            <Modal
                isOpen={isOpen}
                onOpenChange={onOpenChange}
                placement={"center"}
            >
                <ModalContent className="w-80 h-50">
                    {(onClose) => (
                        <>
                            <ModalHeader>
                                <p className="text-red-500 font-bold text-2xl">
                                    Error
                                </p>
                            </ModalHeader>
                            <ModalBody>
                                <p className="text-red-500 text-xl">
                                    Failed to parse QR Code, please try again
                                </p>
                            </ModalBody>
                            <ModalFooter className="flex justify-end">
                                <Button
                                    color="danger"
                                    variant="light"
                                    onPress={onClose}
                                >
                                    Close
                                </Button>
                            </ModalFooter>
                        </>
                    )}
                </ModalContent>
            </Modal>
        </div>
    );
}
