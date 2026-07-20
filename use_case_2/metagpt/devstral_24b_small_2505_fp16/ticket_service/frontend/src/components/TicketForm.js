import React, { useState } from 'react';
import axios from 'axios';
import { useHistory } from 'react-router-dom';

const TicketForm = ({ onTicketCreate }) => {
  const [description, setDescription] = useState('');
  const [status, setStatus] = useState('open');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const history = useHistory();

  // Include all possible statuses from the backend
  const validStatuses = ['open', 'in-progress', 'closed'];

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!validStatuses.includes(status)) {
      setError("Invalid status. Please select a valid status.");
      return;
    }
    setLoading(true);
    try {
      const response = await axios.post('/api/tickets/', { description, status }, {
        headers: { Authorization: `Token ${localStorage.getItem('token')}` }
      });
      onTicketCreate(response.data);
      setDescription('');
      setStatus('open');
    } catch (error) {
      console.error("There was an error creating the ticket!", error);
      if (error.response && error.response.status === 401) {
        localStorage.removeItem('token');
        history.push('/login'); // Use history.push for redirection
      }
      setError("Failed to create a new ticket. Please try again.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <h2>Create New Ticket</h2>
      {error && <p style={{ color: 'red' }}>{error}</p>}
      {loading ? (
        <p>Creating ticket...</p>
      ) : (
        <form onSubmit={handleSubmit}>
          <label>
            Description:
            <input
              type="text"
              value={description}
              onChange={(e) => setDescription(e.target.value)}
              required
            />
          </label>
          <br />
          <label>
            Status:
            <select value={status} onChange={(e) => setStatus(e.target.value)}>
              {validStatuses.map((stat) => (
                <option key={stat} value={stat}>
                  {stat.replace('-', ' ')}
                </option>
              ))}
            </select>
          </label>
          <br />
          <button type="submit" disabled={loading}>Create Ticket</button>
        </form>
      )}
    </div>
  );
};

export default TicketForm;
