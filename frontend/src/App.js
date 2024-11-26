import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [file, setFile] = useState(null);
  const [preview, setPreview] = useState(null);

  const handleUpload = async () => {
    const formData = new FormData();
    formData.append('file', file);

    try {
      const response = await axios.post("http://localhost:8000/upload/", formData, {
        responseType: 'blob'
      });
      const imageBlob = new Blob([response.data]);
      const imageUrl = URL.createObjectURL(imageBlob);
      setPreview(imageUrl);
    } catch (error) {
      console.error("Error uploading the file", error);
    }
  };

  return (
    <div style={{ padding: '20px' }}>
      <h1>AI Image Refinement</h1>
      <input
        type="file"
        onChange={(e) => setFile(e.target.files[0])}
      />
      <button onClick={handleUpload}>Upload</button>
      <div>
        {preview && <img src={preview} alt="Processed" />}
      </div>
    </div>
  );
}

export default App;
