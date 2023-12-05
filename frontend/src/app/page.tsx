'use client'
import React, { useState } from 'react';
import axios from 'axios';

const Home = () => {

  const [selectedFile, setSelectedFile] = useState(null);

  const handleFileChange = (event: any) => {
    setSelectedFile(event.target.files[0]);
  };

  const handleSubmit = async () => {
    if (!selectedFile) {
      alert('Please select a file first!');
      return;
    }

    const formData = new FormData();
    formData.append('file', selectedFile);

    try {
      const response = await axios.post('/api/upload', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });
      console.log(response.data);
      alert('File uploaded successfully');
    } catch (error) {
      console.error('Error uploading file:', error);
      alert('Error uploading file');
    }
  };

  return (
    <div className='flex h-screen items-center justify-center'>
      <div className='flex items-center space-x-4'>
        <input
          type="file"
          onChange={handleFileChange}
          accept="image/*"
          className='border p-2'
        />

        <button
          onClick={handleSubmit}
          className='bg-blue-500 text-white px-4 py-2 rounded'
        >
          Submit Photo
        </button>
      </div>
    </div>
  );
};

export default Home;
