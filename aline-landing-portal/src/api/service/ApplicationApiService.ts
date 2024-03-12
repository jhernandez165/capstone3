import BaseApiService from "./BaseApiService";
import axios, {AxiosResponse} from "axios";
import ApplyResponse from "@api/model/ApplyResponse";
import ApplyRequest from "@api/model/ApplyRequest";

class ApplicationApiService extends BaseApiService {
    constructor() {
        super();
    }

    postApplication(request: ApplyRequest): Promise<AxiosResponse<ApplyResponse>> {
        console.log("Sending application request:", request);
        return axios.post<ApplyRequest, AxiosResponse<ApplyResponse>>("http://localhost:8080/api/applications", request);
    }

}

export default ApplicationApiService;
