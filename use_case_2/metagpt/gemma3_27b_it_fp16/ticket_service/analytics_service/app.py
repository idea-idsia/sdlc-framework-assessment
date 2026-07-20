"""
analytics_service/app.py
This file contains the analytics service for the ticket management system.
It provides functions to generate reports and insights based on ticket data.
"""
import datetime
import logging
from typing import List, Dict, Any

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class AnalyticsService:
    """
    AnalyticsService class provides methods to generate reports and insights
    based on ticket data.
    """

    def __init__(self, ticket_data_source: str = "default_ticket_data",
                 report_data_source: str = "default_report_data"):
        """
        Initializes the AnalyticsService with data sources.

        Args:
            ticket_data_source (str): The source of ticket data. Defaults to "default_ticket_data".
            report_data_source (str): The source of report data. Defaults to "default_report_data".
        """
        self.ticket_data_source: str = ticket_data_source
        self.report_data_source: str = report_data_source
        self.logger: logging.Logger = logging.getLogger(__name__)

    def get_ticket_counts_by_status(self, start_date: datetime.date = datetime.date.min,
                                    end_date: datetime.date = datetime.date.max) -> Dict[str, int]:
        """
        Retrieves the number of tickets for each status within a specified date range.

        Args:
            start_date (datetime.date): The start date for filtering tickets. Defaults to datetime.date.min.
            end_date (datetime.date): The end date for filtering tickets. Defaults to datetime.date.max.

        Returns:
            Dict[str, int]: A dictionary where keys are ticket statuses and values are the corresponding counts.
        """
        try:
            # Simulate fetching ticket data from a data source
            ticket_data: List[Dict[str, Any]] = self._fetch_ticket_data(start_date, end_date)

            status_counts: Dict[str, int] = {}
            for ticket in ticket_data:
                status: str = ticket.get("status", "unknown")
                status_counts[status] = status_counts.get(status, 0) + 1

            self.logger.info(f"Ticket counts by status: {status_counts}")
            return status_counts

        except Exception as e:
            self.logger.error(f"Error getting ticket counts by status: {e}")
            return {}

    def get_average_resolution_time(self, start_date: datetime.date = datetime.date.min,
                                    end_date: datetime.date = datetime.date.max) -> float:
        """
        Calculates the average time taken to resolve tickets within a specified date range.

        Args:
            start_date (datetime.date): The start date for filtering tickets. Defaults to datetime.date.min.
            end_date (datetime.date): The end date for filtering tickets. Defaults to datetime.date.max.

        Returns:
            float: The average resolution time in days.
        """
        try:
            # Simulate fetching ticket data from a data source
            ticket_data: List[Dict[str, Any]] = self._fetch_ticket_data(start_date, end_date)

            total_resolution_time: datetime.timedelta = datetime.timedelta()
            resolved_ticket_count: int = 0

            for ticket in ticket_data:
                if ticket.get("status") == "resolved":
                    created_at: datetime.datetime = ticket.get("created_at")
                    resolved_at: datetime.datetime = ticket.get("resolved_at")

                    if created_at and resolved_at:
                        resolution_time: datetime.timedelta = resolved_at - created_at
                        total_resolution_time += resolution_time
                        resolved_ticket_count += 1

            if resolved_ticket_count > 0:
                average_resolution_time: float = total_resolution_time.total_seconds() / (resolved_ticket_count * 24 * 3600)
                self.logger.info(f"Average resolution time: {average_resolution_time} days")
                return average_resolution_time
            else:
                self.logger.warning("No resolved tickets found within the specified date range.")
                return 0.0

        except Exception as e:
            self.logger.error(f"Error getting average resolution time: {e}")
            return 0.0

    def get_ticket_counts_by_category(self, start_date: datetime.date = datetime.date.min,
                                       end_date: datetime.date = datetime.date.max) -> Dict[str, int]:
        """
        Retrieves the number of tickets for each category within a specified date range.

        Args:
            start_date (datetime.date): The start date for filtering tickets. Defaults to datetime.date.min.
            end_date (datetime.date): The end date for filtering tickets. Defaults to datetime.date.max.

        Returns:
            Dict[str, int]: A dictionary where keys are ticket categories and values are the corresponding counts.
        """
        try:
            # Simulate fetching ticket data from a data source
            ticket_data: List[Dict[str, Any]] = self._fetch_ticket_data(start_date, end_date)

            category_counts: Dict[str, int] = {}
            for ticket in ticket_data:
                category: str = ticket.get("category", "unknown")
                category_counts[category] = category_counts.get(category, 0) + 1

            self.logger.info(f"Ticket counts by category: {category_counts}")
            return category_counts

        except Exception as e:
            self.logger.error(f"Error getting ticket counts by category: {e}")
            return {}

    def _fetch_ticket_data(self, start_date: datetime.date, end_date: datetime.date) -> List[Dict[str, Any]]:
        """
        Simulates fetching ticket data from a data source.

        Args:
            start_date (datetime.date): The start date for filtering tickets.
            end_date (datetime.date): The end date for filtering tickets.

        Returns:
            List[Dict[str, Any]]: A list of dictionaries representing ticket data.
        """
        # Replace this with actual data fetching logic from your data source
        # This is just a placeholder for demonstration purposes
        ticket_data: List[Dict[str, Any]] = [
            {"ticket_id": 1, "created_at": datetime.datetime(2023, 1, 1), "resolved_at": datetime.datetime(2023, 1, 5),
             "status": "resolved", "category": "bug"},
            {"ticket_id": 2, "created_at": datetime.datetime(2023, 1, 2), "resolved_at": datetime.datetime(2023, 1, 7),
             "status": "resolved", "category": "feature"},
            {"ticket_id": 3, "created_at": datetime.datetime(2023, 1, 3), "status": "open", "category": "bug"},
            {"ticket_id": 4, "created_at": datetime.datetime(2023, 1, 4), "resolved_at": datetime.datetime(2023, 1, 8),
             "status": "resolved", "category": "bug"},
        ]
        return ticket_data
