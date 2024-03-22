describe('CRC E2E Test', () => {
    it('Check API', () => {
        cy.request('https://backend-msvsj56xlq-uk.a.run.app/count')
            .then((response) => {
                expect(response.status).to.eq(200)
                expect(response.body).to.have.property('count')
            })
        })
    })