/**
 * frontend/src/components/TicketList.js
 */
import React, { useState, useEffect } from 'react';
import { Ticket } from '../types'; // Assuming types are defined in types.js

interface TicketListProps {
    tickets: Ticket[];
    onTicketStatusChange: (ticketId: number, newStatus: string) => void;
}

const TicketList: React.FC<TicketListProps> = ({ tickets, onTicketStatusChange }) => {
    const [displayedTickets, setDisplayedTickets] = useState<Ticket[]>([]);

    useEffect(() => {
        // Initialize displayed tickets when tickets prop changes
        setDisplayedTickets(tickets);
    }, [tickets]);

    const handleStatusChange = (ticketId: number, newStatus: string) => {
        onTicketStatusChange(ticketId, newStatus);
    };

    return (
        <div>
            <h2>Ticket List</h2>
            {displayedTickets.length === 0 ? (
                <p>No tickets available.</p>
            ) : (
                <ul>
                    {displayedTickets.map((ticket) => (
                        <li key={ticket.ticketId}>
                            <strong>Ticket ID:</strong> {ticket.ticketId}<br />
                            <strong>Title:</strong> {ticket.title}<br />
                            <strong>Status:</strong> {ticket.status}<br />
                            <select
                                value={ticket.status}
                                onChange={(e) => handleStatusChange(ticket.ticketId, e.target.value)}
                            >
                                <option value="open">Open</option>
                                <option value="in progress">In Progress</option>
                                <option value="closed">Closed</option>
                            </select>
                        </li>
                    ))}
                </ul>
            )}
        </div>
    );
};

export default TicketList;
