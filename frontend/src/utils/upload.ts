export default async function uploadFile(file: File) {
    const formData = new FormData();
    formData.append('file', file);
  
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
    } catch (error: any) {
      console.error('Error uploading file:', error);
    }
  }