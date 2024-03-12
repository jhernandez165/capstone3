abstract class BaseApiService {

    private readonly api: string;

    protected constructor() {
        this.api = process.env.REACT_APP_API!;
        console.log(`Base API URL: ${this.api}`);
    }

    protected getApi(endpoint: string) {
        const fullUrl = `${this.api}${endpoint.startsWith("/") ? "" : "/"}${endpoint}`;
        console.log(`Full API URL: ${fullUrl}`);
        return fullUrl;
    }

}

export default BaseApiService;
