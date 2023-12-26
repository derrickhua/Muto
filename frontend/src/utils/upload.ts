export default async function uploadFiles(files: File[]) {
  const formData = new FormData();

  files.forEach((file, index) => {
    formData.append(`files`, file); // Use the same key for all files
  });

  try {
    const response = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/upload`, {
      method: 'POST',
      body: formData,
    });
    
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    const data = await response.json();
    console.log(data); // Process your response here
  } catch (error) {
    console.error('Error uploading files:', error);
  }
}

