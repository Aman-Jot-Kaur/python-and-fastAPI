import React, { useState, useEffect } from 'react';
import axios from 'axios';

type toDoType = {
  Title: string;
  Description: string;
  _id: string;
};

const App = () => {
  useEffect(() => {
    getList();
  }, []);

  const [title, setTitle] = useState('');
  const [desc, setDesc] = useState('');
  const [todo, setTodo] = useState<toDoType[]>([]);
  const [error, setError] = useState<string | null>(null); // State to handle errors

  const getList = async () => {
    try {
      const res = await axios.get('http://127.0.0.1:8000/api/todo');
      setTodo(res.data);
      console.log(todo)
    } catch (error) {
      setError('An error occurred while fetching data.');
    }
  };

  const debouncedSetTodo = debounce((newTodo: toDoType) => {
    setTodo((prevTodo) => [...prevTodo, newTodo]);
  }, 300); // Adjust the debounce delay as needed

  const onsubmithandle = async (e: React.FormEvent) => {
    e.preventDefault();
 let new_id=""
    try {
      const response = await axios.post('http://127.0.0.1:8000/api/todo', {
        Title: title,
        Description: desc,
      });
console.log(response)
     new_id=response.data._id;
      setTitle('');
      setDesc('');
      const newtodo: toDoType = {
        Title: title,
        Description: desc,
        _id: new_id
      };

      debouncedSetTodo(newtodo); // Debounce the setTodo call to improve performance
    } catch (error) {
      console.error('Error:', error);
      setError('An error occurred while adding a new todo.');
    }
  };
  const handleDelete = async (_id: string) => {
    try {
      const response = await axios.delete(`http://127.0.0.1:8000/api/todo/${_id}`);
      const deletedId = response.data._id; // Access the _id from the response
      console.log(deletedId);
  
      // Remove the item from the todo list based on its _id
      setTodo(todo.filter((item) => item._id !== deletedId));
    } catch (error) {
      console.error(error);
    }
  };
  
  

  return (
    <div className='App'>
      <form
        style={{
          display: 'flex',
          flexDirection: 'column',
          gap: '30px',
          alignItems: 'center',
        }}
        onSubmit={(e) => {
          onsubmithandle(e);
        }}
      >
        <h3>add new to-do task</h3>
        <input
          required
          type='text'
          placeholder='title'
          value={title}
          onChange={(e) => {
            setTitle(e.target.value);
          }}
          aria-label='titles'
        />
        <input
          required
          type='text'
          placeholder='description'
          value={desc}
          onChange={(e) => {
            setDesc(e.target.value);
          }}
          aria-label='description'
        />
        <input type='submit' value='Submit' />
        <div style={{display:"flex", flexDirection:"column", gap:"10px"}} >
        {error && <p>{error}</p>}
        {/* Map over the todo array and render each todo item */}
        {todo.map((item: toDoType, index) => (
          <div style={{ flex: "0 1 auto", border:"2px solid black", padding:"3px"}}  key={item._id}>
            <button style={{color:"white", backgroundColor:"red", flex:"end"}} onClick={()=>handleDelete(item._id)}>X</button>
            <h4>{item.Title}</h4>
            <p>{item._id}</p>
            
          </div>
        ))}
      </div>
      </form>
     
    </div>
  );
};

// Debounce function for input fields
function debounce(func: Function, delay: number) {
  let timeoutId: NodeJS.Timeout;
  return (...args: any[]) => {
    clearTimeout(timeoutId);
    timeoutId = setTimeout(() => func(...args), delay);
  };
}

export default App;
