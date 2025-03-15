

export class FormResponse {
    success: boolean 
    data!: object
    
    constructor(success?: boolean, data?: object) {
        this.success = success || false
        this.data = data || {}
    }

    setResponse(success: boolean, data: object) {
        this.success = success
        this.data = data
    }

    getResponse() {
        return {
            success: this.success,
            data: this.data
        }
    }

}
