

import axios from 'axios';
/*
export const getConversation = async () => {
    try {
      const response = await axios.post(
        'https://0165-116-86-212-218.ngrok-free.app/api/conversations',  // Use your ngrok URL here
        {},  // Empty body (as per your original API call)
        {
          headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
           
          },
          maxRedirects: 5,  // Set the maximum number of redirects to follow
        }
      );
      
      // Successfully created conversation, return the response data
      return response.data;
    } catch (error) {
      // If there's an error, log it and rethrow for further handling
      console.error('Error creating conversation:', error);
      throw error;
    }
  };*/

  export const getConversation = async () => {
    try {
      const response = await fetch('https://0165-116-86-212-218.ngrok-free.app/api/conversations', {
        method: 'POST',  // Use POST method
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json',  // Specify JSON content type
        },
        body: JSON.stringify({
          // Your request body data here (example: a message)
          message: "Hello from React using fetch!"
        })
      });
  
      // Check if the response is ok (status code 2xx)
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
  
      // Parse and return the response as JSON
      const data = await response.json();
      return data;
    } catch (error) {
      console.error('Error creating conversation:', error);
      throw error;
    }
  };


  





export const sendPrompt = async (conversationId, prompt) => {
  try {
    const response = await axios.post('http://127.0.0.1:8000/api/conversation/${conversationId}/prompt', {
      prompt,
    });
    return response.data.response;
  } catch (error) {
    console.error('Error sending prompt:', error);
    throw error;
  }
};
