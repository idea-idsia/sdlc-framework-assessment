/**
 * frontend/src/components/TicketDetail.js
 */
import React, { useState, useEffect } from 'react';

interface Ticket {
    ticketId: number;
    title: string;
    description: string;
    status: string;
    createdAt: Date;
    updatedAt: Date;
}

interface TicketDetailProps {
    ticket: Ticket | null;
}

const TicketDetail: React.FC<TicketDetailProps> = ({ ticket }) => {
    const [displayedTicket, setDisplayedTicket] = useState<Ticket | null>(null);

    useEffect(() => {
        // Initialize displayed ticket when ticket prop changes
        setDisplayedTicket(ticket);
    }, [ticket]);

    if (!displayedTicket) {
        return <p>No ticket selected.</p>;
    }

    return (
        <div>
            <h2>Ticket Detail</h2>
            <p><strong>Ticket ID:</strong> {displayedTicket.ticketId}</p>
            <p><strong>Title:</strong> {displayedTicket.title}</p>
            <p><strong>Description:</strong> {displayedTicket.description}</p>
            <p><strong>Status:</strong> {displayedTicket.status}</p>
            <p><strong>Created At:</strong> {displayedTicket.createdAt.toLocaleString()}</p>
            <p><strong>Updated At:</strong> {displayedTicket.updatedAt.toLocaleString()}</p>
        </div>
    );
};

export default TicketDetail;
