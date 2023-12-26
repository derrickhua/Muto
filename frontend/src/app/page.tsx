"use client";
import React, { useState } from 'react';
import uploadFiles from '@/utils/upload'; // Make sure to import the correct function
import { useRouter } from 'next/navigation';

export default function Page(){
  const [selectedFiles, setSelectedFiles] = useState([]);
  const router = useRouter();

  const handleFileChange = (event: any) => {
  
    setSelectedFiles([...event.target.files]);
  };

  const handleSubmit = async () => {
    if (selectedFiles.length === 0) {
      alert('Please select files first!');
      return;
    }
    console.log(selectedFiles)
    try {
      const responses = await uploadFiles(selectedFiles); // Call uploadFiles with the array of files
      console.log(responses);

      // Redirect to the edit page with query params or via state management
      // router.push('/edit');
    } catch (error) {
      console.error('Error uploading files:', error);
      alert('Error uploading files');
    }
  };

  return (
    <div className='flex h-screen items-center justify-center'>
      <div className='flex flex-col items-center space-y-4'>
        <input
          type="file"
          multiple
          onChange={handleFileChange}
          accept="image/*"
          className='border p-2'
        />
        <button
          onClick={handleSubmit}
          className='bg-blue-500 text-white px-4 py-2 rounded'
        >
          Submit Photos
        </button>
      </div>
    </div>
  );
};
