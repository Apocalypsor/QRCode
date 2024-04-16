import { Button } from "@nextui-org/button";
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
        <div className="w-full max-w-md p-4 mx-auto bg-white rounded-xl shadow-md space-y-4 dark:bg-gray-800">
            <h2 className="text-lg font-semibold text-center text-gray-800 dark:text-gray-100">
                {title}
            </h2>
            <div className="flex items-center space-x-2">
                <Button className="w-1/3" type="button">
                    <label className="cursor-pointer">
                        Select File
                        <input
                            type="file"
                            className="hidden"
                            onChange={handleSelect}
                        />
                    </label>
                </Button>
                <div className="border border-gray-300 rounded-lg flex-1 p-2 dark:border-gray-600">
                    <span className="text-sm text-gray-500 dark:text-gray-400">
                        {file ? file.name : "No file selected"}
                    </span>
                </div>
            </div>
            <Button
                className="w-full"
                type="button"
                onClick={handleUpload}
                disabled={!file}
            >
                Upload
            </Button>
        </div>
    );
}
