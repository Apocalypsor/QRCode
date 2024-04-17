import { Button } from "@nextui-org/button";
import { Card, CardBody, CardHeader } from "@nextui-org/card";
import { Input } from "@nextui-org/input";
import { useState } from "react";

export default function FileUploader({
    title,
    onUpload,
}: {
    title: string;
    onUpload: (file: File) => void;
}) {
    const [file, setFile] = useState<File | null>(null);

    const handleSelect = (e: React.ChangeEvent<HTMLInputElement>) => {
        const file = e.target.files ? e.target.files[0] : null;
        if (file) {
            setFile(file);
        }
    };

    const handleUpload = () => {
        if (file) {
            onUpload(file);
        }
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
                    <div className="flex items-center space-x-2">
                        <Button className="w-1/3" type="button">
                            <label className="cursor-pointer">
                                Select File
                                <Input
                                    type="file"
                                    accept="image/jpeg, image/png, image/jpg, image/webp"
                                    className="hidden"
                                    onChange={handleSelect}
                                />
                            </label>
                        </Button>
                        <Input
                            type="text"
                            variant={"faded"}
                            value={file ? file.name : "No File Selected"}
                            isReadOnly
                        />
                    </div>
                    <Button
                        className="w-full mt-4 bg-gradient-to-t from-[#FF1CF7] to-[#b249f8] text-white p-2 rounded-lg hover:bg-violet-800"
                        type="button"
                        onClick={handleUpload}
                        disabled={!file}
                    >
                        Upload
                    </Button>
                </CardBody>
            </Card>
        </div>
    );
}
