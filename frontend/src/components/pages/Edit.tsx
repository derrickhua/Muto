import React, { useState, useEffect } from 'react';
import Image from 'next/image';

export default function EditPage(){
    const [images, setImages] = useState<string[]>([]);

    useEffect(() => {
        // Fetch the list of images from the server
        fetch('http://localhost:8000/images')
            .then(response => response.json())
            .then(data => {
                // Construct the URLs for the images
                const imageUrls = data.images.map((filename: string) => `http://localhost:8000/temp/${filename}`);
                setImages(imageUrls);
            });
    }, []);

    return (
        <div className="flex flex-col h-screen overflow-y-auto p-2">
            {images.map((image, index) => (
                <div key={index} className="relative w-full mb-2 h-60">
                    <Image 
                        src={image} 
                        alt={`Image ${index}`} 
                        layout="fill"
                        objectFit="contain"
                    />
                </div>
            ))}
        </div>
    );
};

