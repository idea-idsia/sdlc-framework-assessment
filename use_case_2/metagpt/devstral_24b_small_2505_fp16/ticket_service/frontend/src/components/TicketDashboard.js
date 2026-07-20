import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Link, useHistory } from 'react-router-dom';

const TicketDashboard = () => {
  const [tickets, setTickets] = useState([]);
  const [loading, setLoading] = useState(true);
  const history = useHistory();

  useEffect(() => {
    const fetchTickets = async () => {
      try {
        const response = await axios.get('/api/tickets/', {
          headers: { Authorization: `Token ${localStorage.getItem('token')}` }
        });
        setTickets(response.data);
      } catch (error) {
        console.error("There was an error fetching the tickets!", error);
        if (error.response && error.response.status === 401) {
          localStorage.removeItem('token');
          history.push('/login');
        }
      } finally {
        setLoading(false);
      }
    };

    fetchTickets();
  }, [history]);

  const handleDelete = async (ticketId) => {
    setLoading(true);
    try {
      await axios.delete(`/api/tickets/${ticketId}/delete/`, {
        headers: { Authorization: `Token ${localStorage.getItem('token')}` }
      });
      setTickets(tickets.filter((ticket) => ticket.id !== ticketId));
    } catch (error) {
      console.error("There was an error deleting the ticket!", error);
      if (error.response && error.response.status === 401) {
        localStorage.removeItem('token');
        history.push('/login');
      }
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <h2>Ticket Dashboard</h2>
      {loading ? (
        <p>Loading tickets...</p>
      ) : (
        <ul>
          {tickets.map((ticket) => (
            <li key={ticket.id}>
              <Link to={`/ticket/${ticket.id}`}>{ticket.description}</Link>
              <button onClick={() => handleDelete(ticket.id)} disabled={loading}>Delete</button>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
};

export default TicketDashboard;
