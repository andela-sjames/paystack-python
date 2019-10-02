"""Script used to define the paystack BulkCharge class."""

from paystackapi.base import PayStackBase


class BulkCharge(PayStackBase):

    @classmethod
    def initiate_bulk_charge(cls, bulkcharge):
        """
        Initiate Bulk Charge.

        {
            "type": "array",
            "description": "",
            "format": ""
        }
        
        Args:
            authorization: Authorization token
            amount: Amount in kobo

        Returns:
            Json data from paystack API.
        """
        return cls().requests.post('bulkcharge', data=bulkcharge)

    @classmethod
    def list(cls, **kwargs):
        """
        List Bulk Charge Batches created by the integration.

        Args:
            perPage: Number of transfer listed per page for pagination
            page: number of pages listed by pagination.

        Returns:
            Json data from paystack API.

        """
        return cls().requests.get('bulkcharge', qs=kwargs,)

    @classmethod
    def fetch_bulk_batch(cls, id_or_code):
        """ This endpoint retrieves a specific batch code.

        It also returns useful information on its progress
        by way of the total_charges and pending_charges attributes.

        Args:
            id_or_code: An ID or code for the transfer whose 
                        details you want to retrieve.
        
        Returns:
            Json data from paystack API
        """
        return cls().requests.get(f"bulkcharge/{id_or_code}")

    @classmethod
    def fetch_charges_batch(cls, id_or_code, **kwargs):
        """
        Fetch the charges associated with a specified batch code.

        Args:
            id_or_code: An ID or code for the batch whose charges you want to retrieve.
            status: pending, success or failed
            perPage: Number of transfers listed per page for pagination
            page: number of pages listed by pagination.

        Returns:
            Json data from paystack API.
        """

        return cls().requests.get(f"bulkcharge/{id_or_code}/charges", qs=kwargs)

    @classmethod
    def pause_bulk_batch(cls, batch_code):
        """
        Pause the proccessing of an ongoing bulk charge batch.

        Args:
            batch_code: code of the batch to be paused

        Returns:
            Json data from the Paystack API.
        """
        return cls().requests.get(f"bulkcharge/pause/{batch_code}")

    @classmethod
    def resume_bulk_charge(cls, batch_code):
        """
        Resume the proccessing of an already paused bulk charge batch.

        Args:
            batch_code: code of the batch to be resumed

        Returns:
            Json data from the Paystack API.
        """
        return cls().requests.get(f"bulkcharge/resume/{batch_code}")
